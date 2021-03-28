import React from 'react'
import { Formik, Field, Form } from 'formik'

const SignUp = () => {
  return (
    <Formik
      initialValues={{ name: "", surname: "", email: "", password: "", age: "", themes: [] }}
      onSubmit={
        async values => {
          console.log(values)
          //   await new Promise(resolve => setTimeout(resolve, 500));
          //   alert(JSON.stringify(values, null, 2));
        }
      }
    >
      <Form class="signup-form">
        <div class="header">
        <p>Name:</p>
        <Field class="label" name="name" type="text" placeholder="" />
        <p>Surname:</p>
        <Field class="label" name="surname" type="text" placeholder="" />
        <p>E-mail:</p>
        <Field class="label" name="email" type="email" placeholder="" />
        <p>Password:</p>
        <Field class="label" name="password" type="password" placeholder="" />
        <p>Age:</p>
        <Field class="label" name="age" type="number" placeholder="" />
        </div>
        <div class="box">
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="university" /> Вселенная
        </label>
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="move" /> Движение
        </label>
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="live" /> Жизнь
        </label>
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="materials" /> Материалы
        </label>
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="matter" /> Материя
        </label>
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="brain" /> Мозг
        </label>
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="science" /> Наука
        </label>
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="energy" /> Энергия
        </label>
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="language" /> Коммуникация
        </label>
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="it" /> IT
        </label>
        </div>
        <p></p>
        <button type="submit">Submit</button>
      </Form>  
    </Formik>
  )
}

export default SignUp
