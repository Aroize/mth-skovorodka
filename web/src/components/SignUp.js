import React from 'react'
import {Formik, Field, Form} from 'formik'

const SignUp = () => {
    return (
        <Formik
        initialValues={{ name: "", surname: "", email: "", password: "", age: "" }}
        onSubmit={
            async values => {
            console.log(values)
        //   await new Promise(resolve => setTimeout(resolve, 500));
        //   alert(JSON.stringify(values, null, 2));
        }
    }
      >
        <Form>
            <p>Name:</p>
          <Field name="name" type="text" placeholder=""/>
          <p>Surname:</p>
          <Field name="surname" type="text" placeholder=""/>
          <p>E-mail:</p>
          <Field name="email" type="email" placeholder=""/>
          <p>Password:</p>
          <Field name="password" type="password" placeholder=""/>
          <p>Age:</p>
          <Field name="age" type="number" placeholder=""/>
          <p></p>
          <button type="submit">Submit</button>
        </Form>
      </Formik>
    )
}

export default SignUp
