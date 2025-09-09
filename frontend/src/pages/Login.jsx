function Login() {
  return (
    <div className="form">
      <h2 className="title">Login</h2>
      <form>
        <input type="text" name="name" id="name" placeholder="👤 Enter your name" />
        <input type="password" name="password" id="password" placeholder="🔑 Enter your password" />
        <button type="submit" className="submit">Login</button>
        <label htmlFor="">Don't have an account ?</label> <a href="./register">Sign Up</a>
      </form>
    </div>
  );
}

export default Login
