import React, { Component } from 'react';
import { Link } from 'react-router-dom'
import GoogleMapReact from 'google-map-react';
import axios from 'axios';
import { Form, Row, Col, Dropdown } from 'react-bootstrap';
import DropdownButton from 'react-bootstrap/DropdownButton';

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
            zoom: 5,
            markers: [],
            mode: null,
            dropDownValue: null,
            dropDownList: [],
            dateInfo: {
                selected: today,
                updated: today
            }
        };
    }

    componentDidMount() {
        this.getGeoLocation();
        this.getMarkerList();
    }

    handleModeSelect = (e) => {
        this.setState({mode: e});
    }

    handleDropDownSelect = (e) => {
        this.setState({dropDownValue: e});
    }

    onDateChange = ([ms]) => {
        this.setState({
            dateInfo: {
                ...this.state.dateInfo,
                selected: new Date(ms)
            }
        });
    }

    onDateUpdate = ([ms]) => {
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

    getMarkerList = () => {
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
                    <Form onSubmit={this.handleSubmit}>
                        <Form.Row>
                            <Col>
                                <DropdownButton
                                    id="dropdown-basic-button"
                                    title={this.state.mode ? this.state.mode : "Select Mode"}
                                    onSelect={this.handleModeSelect}
                                >
                                    <Dropdown.Item eventKey="Arena"> Arena </Dropdown.Item>
                                    <Dropdown.Item eventKey="Team"> Team </Dropdown.Item>
                                </DropdownButton>
                            </Col>
                            <Col>
                                <DropdownButton
                                    id="dropdown-basic-button"
                                    title={this.state.dropDownValue ? this.state.dropDownValue : "Dropdown Button"}
                                    onSelect={this.handleDropDownSelect}
                                >
                                    {this.state.markers.map((marker) => (<Dropdown.Item key={marker.arena_name} eventKey={marker.arena_name}>{marker.arena_name}</Dropdown.Item>))}
                                </DropdownButton>
                            </Col>
                        </Form.Row>
                    </Form>

                    <DateSlider
                        min={start}
                        max={end}
                        selected={this.state.dateInfo.selected}
                        updated={this.state.dateInfo.updated}
                        onChange={this.onDateChange}
                        onUpdate={this.onDateUpdate}
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