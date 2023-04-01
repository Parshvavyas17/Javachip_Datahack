import React from "react";
import { Link } from "react-router-dom";
import { Container, Row, Col, Form, FormGroup, Input } from "reactstrap";
import Helmet from "../components/Helmet/Helmet";
import CommonSection from "../components/UI/CommonSection";
import { useNavigate } from "react-router-dom";
import "../styles/contact.css";

const socialLinks = [
  {
    url: "#",
    icon: "ri-facebook-line",
  },
  {
    url: "#",
    icon: "ri-instagram-line",
  },
  {
    url: "#",
    icon: "ri-linkedin-line",
  },
  {
    url: "#",
    icon: "ri-twitter-line",
  },
];

const Login = () => {
  let navigate = useNavigate();
  return (
    <Helmet title="Register">
      <CommonSection title="Register" />
      <section>
        <Container>
          <Row>
            <Col lg="7" md="7">
              <h6 className="fw-bold mb-4">Register</h6>

              <Form>
                <FormGroup className="Register__form">
                  <Input placeholder="Your Name" type="text" />
                </FormGroup>
                <FormGroup className="Register__form">
                  <Input placeholder="Email" type="email" />
                </FormGroup>
                

                <button onClick={() => { navigate("/"); }} className=" Register__btn" type="submit">
                 Register
                </button>
              </Form>
            </Col>

            <Col lg="5" md="5">
              <div className="Register__info">
                <h6 className="fw-bold">Register Information</h6>
                <p className="section__description mb-0">
                  123 ZindaBazar, Sylhet, Bangladesh
                </p>
                <div className=" d-flex align-items-center gap-2">
                  <h6 className="fs-6 mb-0">Phone:</h6>
                  <p className="section__description mb-0">+88683896366</p>
                </div>

                <div className=" d-flex align-items-center gap-2">
                  <h6 className="mb-0 fs-6">Email:</h6>
                  <p className="section__description mb-0">example@gmail.com</p>
                </div>

                <h6 className="fw-bold mt-4">Follow Us</h6>

                <div className=" d-flex align-items-center gap-4 mt-3">
                  {socialLinks.map((item, index) => (
                    <Link
                      to={item.url}
                      key={index}
                      className="social__link-icon"
                    >
                      <i class={item.icon}></i>
                    </Link>
                  ))}
                </div>
              </div>
            </Col>
          </Row>
        </Container>
      </section>
    </Helmet>
  );
};

export default Login;
