document.addEventListener('DOMContentLoaded', ()=>{
  anime.timeline({
    targets:'.welcome_screen',
    easing:'easeOutExpo',
  })
  .add({
    width:['0vw', '100vw'],
    opacity:['0','1'],
    duration:1700,
  })


  anime({
    targets:'.heading',
    delay:1200,
    opacity:1,
    duration:1500,
    translateY:['-70px', '0px'],
    easing:'easeOutExpo',
  })

  anime({
    targets:'.sub-heading',
    delay:1200,
    opacity:1,
    duration:1500,
    translateY:['-70px', '0px'],
    easing:'easeOutExpo',
  })

  anime({
    targets:'.go-to-home .arrow',
    delay:1500,
    opacity:['0', '1'],
    duration:500,
    translateX:['-50px', '0px'],
    easing:'easeOutExpo',
  })

  anime({
    targets:'.go-to-menu .arrow',
    delay:1800,
    opacity:['0', '1'],
    duration:500,
    translateX:['-50px', '0px'],
    easing:'easeOutExpo',
  })
})
