import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';

const AnyReactComponent = ({ text }) => <div>{text}</div>;

class CampSite extends Component {
    constructor() {
        super();
        this.state = {
            center: {
                'latitude': null,
                'longitude': null
            },
            zoom: 8
        };
    }

    componentDidMount() {
        console.log("didmounaaat");
        this.getGeoLocation();
        fetch('secrets.properties')
            .then((resp) => {
                console.log(resp);
            });
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

    render() {
        return (
            // Important! Always set the container height explicitly
            <div style={{ height: '100vh', width: '100%' }}>
                <GoogleMapReact
                    bootstrapURLKeys={{ key: process.env.GOOGLEAPIKEY}}
                    center={this.state.center}
                    zoom={this.state.zoom}
                >
                    <AnyReactComponent
                        lat={this.state.center.lat}
                        lng={this.state.center.lng}
                        text=<h1>Here</h1>
                    />
                </GoogleMapReact>
            </div>
        );
  }
}

export default CampSite;