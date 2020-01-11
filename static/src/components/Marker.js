import React, { Component } from 'react';


const Marker = (props) => {
    const { color, arena_name, id, } = props;

    return (
        <div className='marker'
            style={{ backgroundColor: color, cursor: 'pointer'}}
            title={arena_name}
            onClick={() => window.open("https://www.google.com", "_blank")}
        />
    );
}

export default Marker