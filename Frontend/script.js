async function checkWebsite(){

const url=document.getElementById("url").value;

const response=await fetch("http://127.0.0.1:8000/predict-url",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

url:url

})

});

const data=await response.json();

document.getElementById("result").innerHTML=data.prediction;

}