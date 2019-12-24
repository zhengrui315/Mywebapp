import React, { Component } from 'react';


const Marker = (props) => {
    const { color, name, id, } = props;

    return (
        <div className='marker'
            style={{ backgroundColor: color, cursor: 'pointer'}}
            title={name}
            onClick={() => window.open("https://www.google.com", "_blank")}
        />
    );
}

export default Marker