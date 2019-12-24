import React, { Component } from 'react';
import axios from 'axios';
import { Button, Form, FormGroup, Label, Input, FormText } from 'reactstrap';


class AddCampSite extends Component {
    onSubmit(e) {
        axios.post('/api/add/campsite', {
            data: {
                'name': '',
                'lat': 0,
                'lng': 0,
                'description': ''
            }
        })
    }

    render() {
        return (
            <div>
                <Form>
                    <FormGroup>
                        <Label for="exampleEmail">Email</Label>
                        <Input type="email" name="email" id="exampleEmail" placeholder="with a placeholder" />
                    </FormGroup>
                </Form>
            </div>
        )
    }
}

export default AddCampSite;