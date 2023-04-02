import React from "react";
import "../../styles/find-car-form.css";
import "../../styles/find-car-form.css";
import { Form, FormGroup } from "reactstrap";

const FindCarForm = () => {
  return (
    <Form className="form">
      <div className=" d-flex align-items-center justify-content-between flex-wrap">
        <FormGroup className="form__group">
          <input type="text" placeholder="Brand" required />
        </FormGroup>

        <FormGroup className="form__group">
          <input type="text" placeholder="Year" required />
        </FormGroup>
        <FormGroup className="form__group">
          <input type="text" placeholder="Owner" required />
        </FormGroup>

        <FormGroup className="select__group" placeholder="Transmission">
          <select>
            <option value="non-ac">Manual</option>
            <option value="non-ac">Automatic</option>
          </select>
        </FormGroup>
        <FormGroup className="form__group">
          <input type="text" placeholder="Fuel Type" required />
        </FormGroup>

        <FormGroup className="form__group">
          <button className="btn find__car-btn">Predict Price</button>
        </FormGroup>
      </div>
    </Form>
  );
};

export default FindCarForm;
