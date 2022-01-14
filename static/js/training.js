function functstart(){
    document.getElementById("work-head").innerHTML = "Workout Time"
    let worktime = document.getElementById("time1").innerHTML
    let breaktime = document.getElementById("break1").innerHTML
    
    let worktimeint = parseInt(worktime);
    let breaktimeint = parseInt(breaktime);

    var hour= Math.floor(worktimeint/60)
    var minute = Math.floor(worktimeint);
    var second = worktimeint*60;
    var secondcahnge = second%60;
 
    minute= minute-1;
    secondcahnge = 60-secondcahnge;
    var count=00;
    var temp=setInterval(function(){
        let clockhour = document.getElementById("clock-hour").innerHTML=hour;
        let clockminute = document.getElementById("clock-minute").innerHTML = minute;
        let clocksecond = document.getElementById("clock-second").innerHTML =secondcahnge;
        if(secondcahnge<00){
            minute=minute-1;
        } 
        secondcahnge=secondcahnge-1;
        if(minute<=00 && hour<=00 && secondcahnge<=00){
            clearInterval(temp);
            return funcbreak();
        }

    },1000)
    
       
    
}
function funcbreak(){
    document.getElementById("work-head").innerHTML = "Break Time";
    let worktime = document.getElementById("time1").innerHTML
    let breaktime = document.getElementById("break1").innerHTML
    let worktimeint = parseInt(worktime);
    let breaktimeint = parseInt(breaktime);
   
    var hour= Math.floor(breaktimeint/60)
    var minute = Math.floor(breaktimeint);
    var second = worktimeint*60;
    var secondcahnge = second%60;
  
    minute= minute-1;
    secondcahnge = 60-secondcahnge;
    var count=0;
    var temp=setInterval(function(){
        let clockhour = document.getElementById("clock-hour").innerHTML=hour;
        let clockminute = document.getElementById("clock-minute").innerHTML = minute;
        let clocksecond = document.getElementById("clock-second").innerHTML =secondcahnge;
        if(secondcahnge<0){
            minute=minute-1;
        } 
        secondcahnge=secondcahnge-1;
        if(minute<=0 && hour<=0 && secondcahnge==0){
            clearInterval(temp);
            return   
        }

    },1000)
}

function funcreset(){
    location.reload(true);
}
function funcplay(){

}
function funcpause(){
    
}

