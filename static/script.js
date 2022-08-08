
    $(document).on('submit','#todo',function(e)
                   {
      // console.log('hello');
      // e.preventDefault();
      $.ajax({
        type:'POST',
        url:'/',
        data:{
            ram:$('#mainram').val(),
            scr:$('#scr').val(),
            company:$('#company').val(),
            typename:$('#typename').val(),
            opsys:$('#opsys').val(),
            cpuname:$('#cpuname').val(),
            resolution:$('#resolution').val(),
            hdd:$('#hdd').val(),
            ssd:$('#ssd').val(),
            gpuname:$('#gpuname').val(),
            touchscreen:$('[name="touchscreen"]').is(':checked'),
            ips:$('[name="ips"]').is(":checked")
        },
        success:function()
        {
            
          //  document.getElementsByClassName("result")[0].setAttribute("style","display:inline");
          //  document.getElementsByClassName("container")[0].setAttribute("style","display:block");
          
        }
      })
    });

 