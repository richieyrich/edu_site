

  var player;
  var video_list;
  //window.onload =()=>{
  //  player = document.getElementById('player');
  //  maintain_ratio()
  //}

  document.onreadystatechange = function(){
    if(document.readyState=='interactive'){
      player = document.getElementById('player')
      video_list = document.getElementById('video_list')
      maintain_ratio()
    }
  }

  function maintain_ratio(){
    var w = player.clientWidth
    var h = w*9/16
    console.log({w,h})
    player.height = h
    video_list.style.maxHeight = h + 'px'
  }

  window.onresize = maintain_ratio
