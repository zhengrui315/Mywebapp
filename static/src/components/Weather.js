import React, { Component } from 'react';
import axios from 'axios';

class Weather extends Component {
    constructor() {
        super();
        this.state = {
            'temp': null,
            'weather': null,
            'time': null
        }
    }

    componentDidMount() {
        setInterval( () => {
          this.setState({
            'time' : new Date().toLocaleString()
          })
        },1000)
        this.getGeoLocation();
    }

    getGeoLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(position => {
                    this.getWeather(position.coords.latitude,  position.coords.longitude);
                })
        } else {
            let errMsg = "Geolocation is not supported by this browser.";
            log.err(errMsg);
            alert(errMsg);
        }
    }

    getWeather(lat, lng) {
        axios.get('/api/main/weather/', {
            params: {
                'lat': lat,
                'lng': lng
            }
        }).then(resp => {
            this.setState({
                'weather': resp.data.weather,
                'temp': resp.data.temp
            });
        }).catch(err => {
            console.log(err);
            alert(err);
        })
    }

    render() {
        return (
            <div className='homepage'>
                <h2 style={{textAlign:"center"}}>{this.state.time}</h2>
                <div className='weather'>
                    {this.state.temp ? (
                        <div className='weather-col'>
                            <div id='fahrenheit'>{this.state.temp.tempF}</div>
                            <div id='celsius'>{this.state.temp.tempC}</div>
                        </div>
                    ) : 'Loading'}

                    {this.state.weather ? (
                        <div className='weather-col'>
                            {Object.entries(this.state.weather).map(([k, v]) => <div key={k}> {k}: {v} </div>)}
                        </div>
                    ) : ''}
                </div>
            </div>
        )
    }
}

export default Weather;