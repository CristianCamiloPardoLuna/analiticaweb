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
  if(!whatsApp.classList.contains('banner-active')){
    let scrollY = document.scrollY;
    setTimeout(
      ()=>{
        whatsApp.classList.add('banner-active');        
      },
      3000
    );
  };
};

validateInput = (e) => {
  let en = e.replace(/\D/g, "");
  let input = document.getElementById("phone");
  input.value = en;
}
