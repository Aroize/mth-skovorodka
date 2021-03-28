import React from 'react'
import {Formik, Field, Form} from 'formik'

const SignIn = () => {



    return (
        <Formik
        initialValues={{ email: "", password: ""}}
        onSubmit={
            async values => {
            console.log(values)
        //   await new Promise(resolve => setTimeout(resolve, 500));
        //   alert(JSON.stringify(values, null, 2));
        }
    }
      >
        <Form class="signin-form">
          <p>E-mail:</p>
          <Field class="label" name="email" type="email" placeholder=""/>
          <p>Password:</p>
          <Field class="label" name="password" type="password" placeholder=""/>
          <button type="submit">Submit</button>
        </Form>
      </Formik>
    )
}

export default SignIn
