$(window).on('load', function() { 
    $( ".container-main .select.select-left .select-text a" )
    .mouseover(function() {
    $( ".container-main" ).removeClass("right-to-center left-to-center left-over left-out right-over right-out").addClass("left-over")
    })
    .mouseleave(function() {
    $( ".container-main" ).removeClass("right-to-center left-to-center left-over left-out right-over right-out").addClass("left-out");
    });
    $( ".container-main .select.select-right .select-text a" )
    .mouseover(function() {
    $( ".container-main" ).removeClass("right-to-center left-to-center left-over left-out right-over right-out").addClass("right-over")
    })
    .mouseleave(function() {
    $( ".container-main" ).removeClass("right-to-center left-to-center left-over left-out right-over right-out").addClass("right-out");
    });


    $( ".container-main .select.select-left .select-text a" )
    .click(function() {
    $( ".container-main" ).removeClass("center left-over left-out right-over right-out").addClass("left-selected")
    })

    $( ".container-main .select.select-right .select-text a" )
    .click(function() {
    $( ".container-main" ).removeClass("center left-over left-out right-over right-out ").addClass("right-selected")
    })


    $(".select-right .select-plus").click(function () {
        $( ".container-main" ).removeClass("left-over left-out right-over right-out left-selected right-selected").addClass("center right-to-center")
    }) 

    $(".select-left .select-plus").click(function () {
        $( ".container-main" ).removeClass("left-over left-out right-over right-out left-selected right-selected").addClass("center left-to-center")
    })
})
