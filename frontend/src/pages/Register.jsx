function Register() {
  return (
    <div className="form">
      <h2 className="title">Sign Up</h2>
      <form>
        <input type="text" name="name" id="name" placeholder="👤 Enter your name" />
        <input type="number" name="number" id="number" placeholder="🆔 Enter your roll number" />
        <input type="number" name="number" id="number" placeholder="🎓 Enter your enrollment number" />
        <input type="password" name="password" id="password" placeholder="🔑 Enter your password" />
        <input type="password" name="password" id="password" placeholder="🔒 Enter your confirm password" />
        <button type="submit" className="submit">Sign Up</button>
        <label htmlFor="">Already have an account? </label> <a href="./login">Login</a>

      </form>
    </div>
  );
}

export default Register