jQuery(function(){

    jQuery('.checklist--item > a').on('click',function(e){
            e.preventDefault();
           
           var temp = jQuery(this).attr('href');     

           if(temp!=='' && temp!=='#') {
                var pos = jQuery(''+temp).offset();
                jQuery('html,body').animate({ scrollTop : pos.top - 100 });

           }

    })

})