import React, { Component } from 'react';
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
            markers: [
                {
                    id: 1,
                    lat: 30.347296600000004,
                    lng: -97.75502259999999
                },
                {
                    id: 2,
                    lat: 30,
                    lng: -97
                }
            ]
        };
    }

    componentDidMount() {
        this.getGeoLocation();
        this.getCampSites();
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
            error => console.log(error);
        }
    }

    getCampSites() {
        axios.get('/api/campsites/')
            .then((resp) => {
                this.setState({markers: resp.data.campsites});
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
                {/* Important! Always set the container height explicitly */}
                <div className='googlemap'>
                    <GoogleMapReact
                        bootstrapURLKeys={{ key: process.env.GOOGLEAPIKEY}}
                        center={this.state.center}
                        zoom={this.state.zoom}
                        yesIWantToUseGoogleMapApiInternals
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
        );
  }
}

export default CampSite;