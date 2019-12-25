import React, { Component } from 'react';
import axios from 'axios';
import { Form, Button } from 'react-bootstrap';
//import Button from 'react-bootstrap/Button';

class AddCampSite extends Component {
    handleSubmit(e) {
        e.preventDefault();
        axios.post('/api/campsite/add/', {
            'name': e.target.elements.name.value,
            'latitude': e.target.elements.lat.value,
            'longitude': e.target.elements.lng.value,
            'description': e.target.elements.description.value
        }).then(resp => {
            console.log(resp);
        }).catch(err => {
            console.log(err);
            alert(err);
        });

    }

    render() {
        return (
            <Form onSubmit={this.handleSubmit}>
              <Form.Group controlId="name">
                <Form.Label>Name</Form.Label>
                <Form.Control type="string" placeholder="name" />
              </Form.Group>
              <Form.Group controlId="lat">
                <Form.Label>Latitude</Form.Label>
                <Form.Control type="string" placeholder="00.0000" />
              </Form.Group>
              <Form.Group controlId="lng">
                <Form.Label>Longitude</Form.Label>
                <Form.Control type="string" placeholder="00.0000" />
              </Form.Group>
              <Form.Group controlId="description">
                <Form.Label>Description</Form.Label>
                <Form.Control as="textarea" rows="3" placeholder="park name, nearby city, etc" />
              </Form.Group>
              <Button type="submit"> Submit </Button>
            </Form>
        )
    }
}

export default AddCampSite;