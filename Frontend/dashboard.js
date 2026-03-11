async function loadTraffic(){

let response = await fetch("http://127.0.0.1:5000/gettraffic");

let data = await response.json();

let counts = data.map(d=>d.vehicle_count);
let locations = data.map(d=>d.location);

let alertMessage = "";

data.forEach(d => {
    if(d.status === "High Traffic"){
        alertMessage = "🚨 High Traffic at " + d.location;
    }
});

document.getElementById("alert").innerHTML = alertMessage;

let ctx = document.getElementById("trafficChart");

new Chart(ctx,{
type:"bar",

data:{
labels:locations,

datasets:[{
label:"Vehicle Count",
data:counts
}]
}

});

}

setInterval(loadTraffic,3000);