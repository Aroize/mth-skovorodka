import React from 'react'
import { Formik, Field, Form } from 'formik'
import axios from 'axios'

const SignUp = () => {

  return (
    <Formik
      initialValues={{ name: "", surname: "", email: "", password: "", age: "", themes: [] }}
      onSubmit={
        async values => {
          console.log(values)
          axios.post(`https://stark-chamber-07526.herokuapp.com/user.register?email=${values.email}&pwd=${values.email}&name=${values.name}&surname=${values.surname}&age=${values.age}`)
          .then((resp) => { 
            console.log(resp)
            if (resp.statusText === 200) {
              axios.post(`https://stark-chamber-07526.herokuapp.com/user.pickThemes?uid=${resp.result.id}}&themes=${values.toString()}`)
              .then((res) => { 
                console.log(res)
              })  
            }
          })
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
          <Field type="checkbox" class="checkbox" name="themes" value="0" /> Вселенная
        </label>
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="1" /> Движение
        </label>
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="2" /> Жизнь
        </label>
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="3" /> Материалы
        </label>
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="4" /> Материя
        </label>
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="5" /> Мозг
        </label>
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="6" /> Наука
        </label>
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="7" /> Энергия
        </label>
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="8" /> Коммуникация
        </label>
        <label>
          <Field type="checkbox" class="checkbox" name="themes" value="9" /> IT
        </label>
        </div>
        <p></p>
        <button type="submit">Submit</button>
      </Form>  
    </Formik>
  )
}

export default SignUp
