function createFreq(){
    let value=document.getElementById("input_freq").value;
    if(value){
        url=`/app/frequency/${value}`;
    }else{
        url=`/app/frequency/500`;
    }
    window.location.href=url;
}
function createTresh(){
    let value=document.getElementById("input_threshold").value;
    if(value){
        url=`/app/threshold/${value}`;
    }else{
        url=`/app/threshold/100`;
    }
    window.location.href=url;
}
