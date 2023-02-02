import React from 'react';
import { useForm } from 'react-hook-form';
import { useState } from 'react';
import './App.css';
import axios from 'axios';
import * as yup from "yup";
import { yupResolver } from "@hookform/resolvers/yup";
import './App.css';
import PriceComponent from './components/DeliveryPrice';


const schema = yup.object().shape({
  // Validator for cart value.
  cartValue: yup.number()
  .typeError('Must be a number')
  .required('Please Enter your cart value')
  .positive('Must be a positive number'),

  // Validator for distance.
  distance: yup.number()
  .typeError('Must be a number')
  .required('Please Enter the distance you are from the store in meters')
  .positive('Must be a positive number'),

  // Validator for number of items.
  number_of_items: yup.number()
  .typeError('Must be a integer number')
  .required('Please Enter the number of items in your cart')
  .positive('Must be a positive integer number')
  .integer('Must be a integer number'),

  // Validator for time.
  time: yup.string()
  .typeError('It must have this format "12:00", not 12h00')
  .required('Please Enter the number of items in your cart')
  ,

});


function Form() {

  const [response, setResponse] = useState(null);

  const {register, handleSubmit, formState: { errors }, reset } = useForm({
    resolver: yupResolver(schema),
  });

  const onSubmit = async(data) => {
    console.log(data);
  
    try {
      // Make axios post request.
      const response = await axios({
        method: "post",
        url: "http://localhost:8000/api/deliveryinfo/calculate",
        data: data,
      });
      console.log('Delivery Price:', response.data);
      setResponse(response.data);
    } catch (error) {
      console.error('Error:', error.response.data);
    }
  }

  return (
      <>
        <div className='form-container'>
          <form onSubmit={handleSubmit(onSubmit)}>
            <h1>Delivery Fee Calculator</h1>
            <label>
              Cart Value:
              <input type="cartValue" {...register("cartValue")} placeholder=" 20" required/>
              <p className='euro'>€</p>
              <p className="errorMessage">{errors.cartValue?.message}</p>
            </label>
            <label>
              Delivery distance:
              <input type="distance" {...register("distance")} placeholder=" 900" required/>
              <p className='meters'>m</p>
              <p className="errorMessage">{errors.distance?.message}</p>
            </label>
            <label>
              Amount of items:
              <input type="number_of_items" {...register("number_of_items")} placeholder=" 1" required/>
              <p className="errorMessage">{errors.number_of_items?.message}</p>
            </label>
            <label>
              Time:
              <input type="text" {...register("time")} placeholder=" 12:00" required/>
              <p className="errorMessage">{errors.time?.message}</p>
            </label>
            <button className='button' type="submit">Calculate delivery price</button>
          </form>
          <PriceComponent response={response} />
          <div className='bottomCard'></div>
        </div>
        <footer>
          <h2 className='footerPhrase'>
            This site was fully developed and styled by <a href="http://www.devhbo.com">Hassan Bittencourt</a>, using Python Django Framework and ReactJS.
          </h2>
        </footer>
      </>
  );
}

export default Form;
