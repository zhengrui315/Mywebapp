import React, { Component } from 'react';
import { Link } from 'react-router-dom'
import GoogleMapReact from 'google-map-react';
import axios from 'axios';

import Marker from './Marker';
import DateSlider from './DateSlider/DateSlider';

class NBAMap extends Component {
    constructor() {
        super();

        const today = new Date();
        this.state = {
            center: {
                'latitude': null,
                'longitude': null
            },
            zoom: 8,
            markers: [],
            dateInfo: {
                selected: today,
                updated: today
            }
        };
    }

    componentDidMount() {
        this.getGeoLocation();
        this.getNBAArena();
    }

    onChange = ([ms]) => {
        this.setState({
            dateInfo: {
                ...this.state.dateInfo,
                selected: new Date(ms)
            }
        });
    }

    onUpdate = ([ms]) => {
        this.setState({
            dateInfo: {
                ...this.state.dateInfo,
                updated: new Date(ms)
            }
        });
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
        {/* month Integer value representing the month, beginning with 0 for January to 11 for December. */}
        const start = new Date(2019, 9, 22);
        const end = new Date(2020, 4, 22);

        return (
            <div>
                <div>
                    <DateSlider
                        min={start}
                        max={end}
                        selected={this.state.dateInfo.selected}
                        updated={this.state.dateInfo.updated}
                        onChange={this.onChange}
                        onUpdate={this.onUpdate}
                    />
                </div>
                <div>

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