let s_btn = document.getElementById('s_btn')
let form = document.getElementById('data_in')



form.addEventListener('submit',function(e){
    e.preventDefault()

    let nme = document.getElementById('name').value
    let pic = document.getElementById('picture').files[0]

    if(nme==""){
        document.getElementById('name_error').innerHTML= "Name Cannot Be Empty";
        return false
    }else if(!pic){
        document.getElementById('picture_error').innerHTML="Picture Cannot Be Empty";
        return false
    }

    else{
        let fd = new FormData()
        fd.append("name",nme);
        fd.append("image",pic)
        fd.append("csrfmiddlewaretoken",'{csrf_token}')

        let url = '/uploads/';

        fetch(url,{
            method:"POST",
            body:fd,
        })
        .then(function(result){
            result.json()
            return result
        })

        .then(function(data){
            console.log("success",data);
        })
        .catch(function(error){

            console.log(error);

        
        });


        

        
    }

    
    

})

