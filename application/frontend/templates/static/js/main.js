try{
  var navbar1 = document.getElementById("navbar-1-ul");
  var btnContainer = navbar2.getElementById("navbar");
  var btns = btnContainer.getElementsByClassName("nav-item");
  for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function() {
      var current = document.getElementsByClassName("active");
      current[0].className = current[0].className.replace(" active", "");
      this.className += " active";
    });
  } 
}catch{
  //
};

var whatsApp = document.getElementById('whatsapp');
window.onscroll = () =>{
  if(! whatsApp.classList.contains('banner-active')){
    setTimeout(
      ()=>{
        whatsApp.classList.add('banner-active');        
      }, 
      3000
    );
  }
}