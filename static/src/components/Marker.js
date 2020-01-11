import React, { Component } from 'react';


const K_SIZE = 20;

const markerStyle = {
  // initially any map object has left top corner at lat lng coordinates
  // it's on you to set object origin to 0,0 coordinates
  position: 'absolute',
  width: K_SIZE,
  height: K_SIZE,
  left: -K_SIZE / 2,
  top: -K_SIZE / 2,

  border: '',
  borderRadius: K_SIZE,
  backgroundColor: 'blue',
  textAlign: 'center',
  color: '#3f51b5',
  fontSize: 10,
  fontWeight: 'bold',
  padding: 4,
  cursor: 'pointer'
};

const markerHoverStyle = {
    ...markerStyle,
    fontSize: 16
}

class Marker extends Component {
    constructor(props) {
        super(props);
    }


    handleClick() {
        window.open("https://www.google.com", "_blank");
    }

    render() {
        const { color, arena_name, id, } = this.props;

        {/* GoogleMap passes a $hover prop to hovered components. To detect hover it an uses internal mechanism */}
        const style = this.props.$hover ? markerHoverStyle : markerStyle;
        console.log("hover status: ", this.props.$hover);
        return (
            <div className='marker'
                style={style}
                title={arena_name}
                onClick={this.handleClick}
            >
                {this.props.$hover ? this.props.arena_name : ''}
            </div>
        )
    }
}

export default Marker;