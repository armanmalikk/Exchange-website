$(document).ready(function(){
    
	//side menu for mobile
	$("#side-menu-button").click(function(){
      $('#side-menu').css("width","250px");

    })

    $("#close-buttion-top").click(function(){
      $('#side-menu').css("width","0px");
      $('#main').css("marginLeft","0px");
    })
    
    

    ///////////////////////////click the confirm payment
    $(document).on('click', '.online-the-popup' ,function(){ 
    	$("body").css("overflow","hidden")
    	$("#onlick-traing-fixed-body").css("display","block")
    })


    ///////////////////////////click the close payment
    $(".popup-close").click(function(){
    	$("body").css("overflow","auto")
    	$("#onlick-traing-fixed-body").css("display","none")
    })


    ///////////////////////////////////////click the ul li second-list
    $(".first-list").click(function(){
    	$(".first-list").removeClass("active-li")
    	$(this).addClass("active-li")
    })

	///////////////////////////////////////click the ul li 
    $(document).on('click', '.second-list' ,function(){ 
    	$(".second-list").removeClass("active-li")
    	$(this).addClass("active-li")
    })



    ///////////////////////////////////////////////////////////////////////////////////////calculator
     var firstInput=1;
     var firstAttrName="NONE";
     var secondAttrName="NONE";
     var firstPrice;
     var secondPrice;
     var exchangeValue = 2;
     var finalAmount;
     var getImg1="";
     var getImg2="";

     var formFistValue = "1"
     var formFinalValue = "2"


    /////////////////////input keyup
    $(".calculator-input").change(function(){
    	firstInput = $(this).val()

        formFistValue =  firstInput

        finalAmount = (firstInput*secondPrice).toFixed(1) 
        $(".receive-amount-text").html(finalAmount)
    }) 
    
    /////////////////////click the first list
    $(".first-list").click(function(){
    	firstAttrName = $(this).attr("data-name")
      firstAttrId = $(this).attr("data-id")
      firstPrice = $(this).attr("data-price")
    	getImg1 = $('.first-list-img',this).attr("src")
    	$(".first-chang-title").html(firstAttrName)	
        $(".remove-the-shadow").removeClass("not-allow-title")
    })

    /////////////////////click the second list
    $(document).on('click', '.second-list' ,function(){ 
      secondAttrName = $(this).attr("data-name")
      secondAttrId = $(this).attr("data-id")
      secondPrice = $(this).attr("data-price")
      getImg2 = $('.second-list-img',this).attr("src")
      $(".second-chang-title").html(secondAttrName)
      finalAmount = (firstInput*secondPrice).toFixed(1) 

      formFinalValue = finalAmount

      $(".receive-amount-text").html(finalAmount)
      console.log(secondPrice)

      $(".confirm-payment").addClass("online-the-popup")

    })


    ///////////////////////////////////////////////////////click the popup function


        $(document).on('click', '.online-the-popup' ,function(){    
            $(".popup-first-value").html(firstInput)
            $(".popup-second-value").html(finalAmount)
            $(".pop-fisrt-text").html(firstAttrName)
            $(".pop-second-text").html(secondAttrName)
            $(".pop-fisrt-img").attr('src', getImg1);
            $(".pop-second-img").attr('src', getImg2);

            /////////////////////////////////////////////////////////form

            $(".form-send-amount").val(formFistValue)
            $(".form-receive-amount").val(formFinalValue)
            $(".form-send-name").val(firstAttrId)
            $(".form-receive-name").val(secondAttrId)
        })


        $('.calculator-title').click(function(e){

              swal({
                title: "Auto close alert!",
                text: "I will close in 2 seconds.",
                icon: "success",
                timer: 2000
              });    

        });

        $(".login-main-title").click(function(e){

              swal({
                title: "Successful!!!",
                text: "Your message Successful post.",
                icon: "success",
                timer: 2000
              });    

        });

    

})


///////////////when scroll
$(window).scroll(function() {
    if ($(this).scrollTop() > 30) { // this refers to window
        $("#menu-bar").css('margin-top',"-40px");
    }else{
    	$("#menu-bar").css('margin-top',"0px");
    }
});
