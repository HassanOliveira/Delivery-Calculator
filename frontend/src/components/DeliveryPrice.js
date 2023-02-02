import React from 'react';

class PriceComponent extends React.Component {
  render() {
    return (
      <div>
        <h2 className='deliveryPrice'>Delivery Price: {this.props.response} €</h2>
      </div>
    );
  }
}

export default PriceComponent;