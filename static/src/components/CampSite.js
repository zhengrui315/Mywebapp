import React, { Component } from 'react';
import { Link } from 'react-router-dom'
import GoogleMapReact from 'google-map-react';
import axios from 'axios';

import Marker from './Marker';

class CampSite extends Component {
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
        this.getCampSites();
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

    getCampSites() {
        axios.get('/api/campsites/')
            .then((resp) => {
                this.setState({markers: [...this.state.markers, ...resp.data.campsites]});
            })
            .catch((err) => {
                console.log(err);
            })
    }

    render() {
        return (
            <div>
                <form className="form-inline md-form form-sm mt-0">
                    <input className="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search"
                        aria-label="Search"/>
                    <button className="btn btn-outline-warning btn-rounded btn-sm my-0" type="submit">Search</button>
                </form>
                <div>
                    <div className='map-sidebar'>
                        <Link to='/campsite_add/'><button> add new </button></Link>
                    </div>
                    {/* Important! Always set the container height explicitly */}
                    <div className='googlemap'>
                        <GoogleMapReact
                            bootstrapURLKeys={{ key: process.env.GOOGLEAPIKEY}}
                            center={this.state.center}
                            zoom={this.state.zoom}
                            yesIWantToUseGoogleMapApiInternals
                            options={this.createMapOptions}
                        >
                            {this.state.markers.map(marker => (
                                <Marker
                                    key={marker.id}
                                    lat={marker.lat}
                                    lng={marker.lng}
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

export default CampSite;