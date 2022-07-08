from django.apps import AppConfig


class App1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'


"""<form action="{% url 'register' %}">
    {% csrf_token %}
    {{ n }}
  <div class="container">
    <h1>Register</h1>
    <p>Please fill in this form to create an account.</p>
    <hr>
      <label for="name"><b>Name</b></label>
    <input type="text" placeholder="UserName" name="name" id="name" required>
    <br><br>
    <label for="mobile"><b>Mobile</b></label>
    <input type="text" placeholder="Mobile" name="mobile" id="mobile" required>
    <br><br>
    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email" name="email" id="email" required>
    <br><br>
    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="password" id="psw" required>
    <br><br>
    <label for="confirm Password"><b>Confirm Password</b></label>
    <input type="password" placeholder="Repeat Password" name="Confirm_password" id="psw-repeat" required>
      <br><br>
      <p>By creating an account you agree to our <a href="#">Terms & Privacy</a>.</p>
    <button type="submit" class="registerbtn">Register</button>
  </div>
    <hr>


  </div>

  <div class="container signin">
    <p>Already have an account? <a href="#">log in</a>.</p>
  </div>
</form>"""