import sys
from enum import Enum

class PercentageMode(Enum):
    Increasing = 0
    Decreasing = 1

def generate_percentage(
    percentage=0, 
    degree=141, 
    color_left="black", 
    color_right="transparent", 
    start_percentage=50):
    return """
    {percentage}%  {{ background-image: repeating-linear-gradient({degree}deg, {color_left}, {color_left} {start_percentage}%, {color_right} 0%, {color_right} 100%); }}""" \
    .format(
        percentage=percentage, 
        degree=degree, 
        color_left=color_left, 
        color_right=color_right, 
        start_percentage=str(start_percentage)
    )

def generate_percentages(
    degree=141, 
    color_left="black", 
    color_right="transparent", 
    start_percentage=50,
    from_percentage=0, 
    to_percentage=100, 
    change=10, 
    step=1, 
    mode=PercentageMode.Increasing):
    change_float = float(change)
    percentages_string = ""

    percentage = start_percentage
    
    change = change_float / (to_percentage - from_percentage) * step
    for p in range(from_percentage, to_percentage + 1, step):
        percentage_string = "{0:.2f}".format(percentage)
        percentages_string += generate_percentage(
            percentage=p, 
            degree=degree, 
            color_left=color_left, 
            color_right=color_right, 
            start_percentage=percentage_string)
        if mode == PercentageMode.Increasing:
            percentage += change
        else:
            percentage -= change

    return percentages_string


def generate_keyframes(
    function_type,
    function_name='function_name',
    degree=141, 
    color_left="black", 
    color_right="transparent", 
    start_percentage=50,
    from_percentage=0, 
    to_percentage=100, 
    change=10, 
    step=1, 
    mode=PercentageMode.Increasing):
    function_css = generate_percentages(
        step= step,
        degree=degree, 
        color_left=color_left, 
        color_right=color_right, 
        start_percentage=start_percentage,
        from_percentage=from_percentage, 
        to_percentage=to_percentage, 
        change=change,
        mode=mode)
    return """{function_type} {function_name} {{ {function_css} 
}}
""".format(
    function_type=function_type, 
    function_name = function_name, 
    function_css=function_css
)

def generate_class(
    class_name='.some-class',
    function_name='function_name',
    duration=0.1,
    timing_function= 'linear',
    delay= 0,
    iterations=1,
    direction= 'normal',
    degree=141,
    color_left="black", 
    color_right="transparent", 
    start_percentage=50,
    mode=PercentageMode.Increasing,
    change=10):

    final_percentage = start_percentage
    if mode == PercentageMode.Increasing:
        final_percentage += change
    else:
        final_percentage -= change

    return """{class_name} {{
    -webkit-animation: {function_name} {duration}s {timing_function} {delay}s {iterations} {direction}; /* Safari 4+ */
    -moz-animation:    {function_name} {duration}s {timing_function} {delay}s {iterations} {direction}; /* Fx 5+ */
    -o-animation:      {function_name} {duration}s {timing_function} {delay}s {iterations} {direction}; /* Opera 12+ */
    animation:         {function_name} {duration}s {timing_function} {delay}s {iterations} {direction}; /* IE 10+, Fx 29+ */
    background-image:  repeating-linear-gradient({degree}deg, {color_left}, {color_left} {final_percentage}%, {color_right} 0%, {color_right} 100%);
}}
    """.format(
        class_name=class_name, 
        function_name=function_name, 
        duration=duration, 
        timing_function=timing_function, 
        delay= delay,
        iterations=iterations, 
        direction=direction,
        degree=degree, 
        color_left=color_left, 
        color_right=color_right, 
        final_percentage=str(final_percentage)
    )



def generate_transition_css(
    class_name='.some-class',
    function_name='function_name',
    duration=0.1,
    timing_function= 'linear',
    delay= 0,
    iterations=1,
    direction= 'normal',
    degree=141,
    color_left="black", 
    color_right="transparent", 
    start_percentage=50,
    mode=PercentageMode.Increasing,
    change=10,
    from_percentage=0, 
    to_percentage=100,
    step=1
    ):
    print(generate_class(
        class_name=class_name,
        function_name=function_name,
        duration=duration,
        timing_function= timing_function,
        delay= delay,
        iterations=iterations,
        direction= direction,
        degree=degree,
        color_left=color_left, 
        color_right=color_right, 
        start_percentage=start_percentage,
        mode=mode,
        change=change
    ))

    keyframes_types = ['@-webkit-keyframes', '@-moz-keyframes','@-o-keyframes', '@keyframes'] 
    for types in keyframes_types:
        print(generate_keyframes(
            function_type=types,
            function_name=function_name,
            degree=degree, 
            color_left=color_left, 
            color_right=color_right, 
            start_percentage=start_percentage,
            from_percentage=from_percentage, 
            to_percentage=to_percentage, 
            change=change, 
            step=step, 
            mode=mode
        ))



if __name__ == "__main__":
    print('Supplied args...')
    for arg in sys.argv[1:]:
        print(arg)

    degree=141
    color_left="black"
    color_right="transparent"
    step=5
    change=10
    timing_function= 'ease-out'

    print('CSS generation started ...')

    # left hover
    generate_transition_css(
        class_name='.container-main.center.left-over',
        function_name='expand-left',
        timing_function= timing_function,
        degree=degree,
        color_left=color_left, 
        color_right=color_right, 
        start_percentage=50,
        mode=PercentageMode.Increasing,
        change=change,
        step=step
    )

    generate_transition_css(
        class_name='.container-main.center.left-out',
        function_name='contract-left',
        timing_function= timing_function,
        degree=degree,
        color_left=color_left, 
        color_right=color_right, 
        start_percentage=60,
        mode=PercentageMode.Decreasing,
        change=change,
        step=step
    )


    # right hover
    generate_transition_css(
        class_name='.container-main.center.right-over',
        function_name='expand-right',
        timing_function= timing_function,
        degree=degree,
        color_left=color_left, 
        color_right=color_right, 
        start_percentage=50,
        mode=PercentageMode.Decreasing,
        change=change,
        step=step
    )

    generate_transition_css(
        class_name='.container-main.center.right-out',
        function_name='contract-right',
        timing_function= timing_function,
        degree=degree,
        color_left=color_left, 
        color_right=color_right, 
        start_percentage=40,
        mode=PercentageMode.Increasing,
        change=change,
        step=step
    )
    
    # right select
    generate_transition_css(
        class_name='.container-main.left-selected',
        function_name='center-full-expand-right',
        timing_function= timing_function,
        degree=degree,
        color_left=color_left, 
        color_right=color_right, 
        start_percentage=60,
        mode=PercentageMode.Increasing,
        change=35,
        step=step
    )

    # right select
    generate_transition_css(
        class_name='.container-main.right-selected',
        function_name='center-full-expand-left',
        timing_function= timing_function,
        degree=degree,
        color_left=color_left, 
        color_right=color_right, 
        start_percentage=40,
        mode=PercentageMode.Decreasing,
        change=35,
        step=step
    )

    generate_transition_css(
        class_name='.container-main.center.right-to-center',
        function_name='right-to-center',
        timing_function= timing_function,
        degree=degree,
        color_left=color_left, 
        color_right=color_right, 
        start_percentage=95,
        mode=PercentageMode.Decreasing,
        change=45,
        step=step
    )

    generate_transition_css(
        class_name='.container-main.center.left-to-center',
        function_name='left-to-center',
        timing_function= timing_function,
        degree=degree,
        color_left=color_left, 
        color_right=color_right, 
        start_percentage=5,
        mode=PercentageMode.Increasing,
        change=45,
        step=step
    )

    print('CSS generation finished!')
