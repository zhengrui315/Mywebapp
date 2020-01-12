import React, { Component } from 'react';
import { Link } from 'react-router-dom'
import GoogleMapReact from 'google-map-react';
import axios from 'axios';

import Marker from './Marker';
import DateSlider from './DateSlider/DateSlider';

class NBAMap extends Component {
    constructor() {
        super();
        this.state = {
            center: {
                'latitude': null,
                'longitude': null
            },
            zoom: 8,
            markers: []
        };
    }

    componentDidMount() {
        this.getGeoLocation();
        this.getNBAArena();
    }

    createMapOption(maps) {
        return({
            disableDefaultUI: true,
            streetViewControl: false,
            panControl: false,
            mapTypeControl: true,
            scrollwheel: true,
            styles: [{ stylers: [{ 'saturation': -100 }, { 'gamma': 0.8 }, { 'lightness': 4 }, { 'visibility': 'on' }] }]
        })
    }

    getGeoLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(position => {
                this.setState({
                    center: {
                        lat: position.coords.latitude,
                        lng: position.coords.longitude
                    }
                });
            })
        } else {
            let errMsg = "Geolocation is not supported by this browser.";
            log.err(errMsg);
            alert(errMsg);
        }
    }

    getNBAArena() {
        axios.get('/api/nba/arena/')
            .then((resp) => {
                this.setState({markers: [...this.state.markers, ...resp.data.arena_list]});
            })
            .catch((err) => {
                console.log(err);
            })
    }

    render() {
        return (
            <div>
                <div>
                    <form className="form-inline md-form form-sm mt-0">
                        <input className="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search"
                            aria-label="Search"/>
                        <button className="btn btn-outline-warning btn-rounded btn-sm my-0" type="submit">Search</button>
                        <Link to='/campsite_add/' id="add-new"><button className="btn btn-outline-warning btn-rounded btn-sm my-0"> add new </button></Link>
                    </form>
                </div>
                <div>
                    <div className='map-sidebar'>

                    </div>
                    {/* Important! Always set the container height explicitly */}
                    <div className='googlemap'>
                        <GoogleMapReact
                            bootstrapURLKeys={{ key: process.env.GOOGLEAPIKEY}}
                            center={this.state.center}
                            zoom={this.state.zoom}
                            yesIWantToUseGoogleMapApiInternals
                            options={this.createMapOptions}
                            hoverDistance={100}
                        >
                            {this.state.markers.map(marker => (
                                <Marker
                                    key={marker.team_name}
                                    arena_name={marker.arena_name}
                                    lat={marker.latitude}
                                    lng={marker.longitude}
                                    team_name={marker.team_name}
                                    color={'blue'}
                                />
                            ))}
                        </GoogleMapReact>
                    </div>
                </div>
            </div>
        );
  }
}

export default NBAMap;