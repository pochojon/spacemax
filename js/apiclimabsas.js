  // consumo de API ope-meteo.com
  var txt = ""
  fetch("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&timezone=America/Argentina/Buenos_Aires&current_weather=true&daily=apparent_temperature_min&daily=apparent_temperature_max&daily=windspeed_10m_max")
.then(response => response.text())      
.then(json => {                    
    //parseo lo que devuelve la api del tiempo para la ciudad de Buenos Aires y me quedo con los datos de temperatura de hoy, 24 y 48 hs
    
    txt = JSON.parse(json); 
    console.log(txt)
    console.log(txt.current_weather.temperature)
    console.log(txt.current_weather.windspeed)
    console.log(txt.daily.time[1])
    console.log(txt.daily.apparent_temperature_min[0])
    console.log(txt.daily.apparent_temperature_max[0])
    console.log(txt.daily.windspeed_10m_max[1])
 

    // lleno los valores segun vector diasemana con sus temperaturas minimnas y maximas
    const diassemana = ['lunes','martes','miércoles','jueves', 'viernes','sabado','domingo']
    document.getElementById("temperaturaactual").innerHTML = "Temperatura actual: "+txt.current_weather.temperature+"º"
    document.getElementById("velocidadviento").innerHTML = "Vientos: "+txt.current_weather.windspeed+ "Km/h"
    
    document.getElementById("hoy").innerHTML = "Hoy "+ diassemana[new Date(txt.daily.time[0]).getDay()].toUpperCase()
    document.getElementById("hoyminima").innerHTML = "T Min: "+txt.daily.apparent_temperature_min[0]+"º"
    document.getElementById("hoymaxima").innerHTML = "T Max: "+txt.daily.apparent_temperature_max[0]+"º"

    document.getElementById("manana").innerHTML = diassemana[new Date(txt.daily.time[1]).getDay()].toUpperCase()
    document.getElementById("mananavientos").innerHTML = "Vientos: "+txt.daily.windspeed_10m_max[1]+"Km/h"
    document.getElementById("mananaminima").innerHTML = "T Min: "+txt.daily.apparent_temperature_min[1]+"º"
    document.getElementById("mananamaxima").innerHTML = "T Max: "+txt.daily.apparent_temperature_max[1]+"º"
    

    document.getElementById("pasadomanana").innerHTML = diassemana[new Date(txt.daily.time[2]).getDay()].toUpperCase()
    document.getElementById("pasadovientos").innerHTML = "Vientos: "+txt.daily.windspeed_10m_max[2]+"Km/h"
    document.getElementById("pasadomananaminima").innerHTML = "T Min: "+txt.daily.apparent_temperature_min[2]+"º"
    document.getElementById("pasadomananamaxima").innerHTML = "T Max: "+txt.daily.apparent_temperature_max[2]+"º"
   
})
.catch(error => {                  // 3
    // handle error
});

