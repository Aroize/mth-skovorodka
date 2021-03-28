package ru.ilia.kgraph

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class LoginActivity: AppCompatActivity() {

    private lateinit var signInEmail: EditText
    private lateinit var signInPwd: EditText
    private lateinit var signInBtn: Button
    private lateinit var signUpBtn: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_auth)
        signInEmail = findViewById(R.id.sign_in_email)
        signInPwd = findViewById(R.id.sign_in_pwd)
        signInBtn = findViewById(R.id.sign_in)
        signUpBtn = findViewById(R.id.sign_up)
    }
}