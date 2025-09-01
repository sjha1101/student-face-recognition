function App() {
  return (
    <div className="form">
      <h2 className="title">Login</h2>
      <form>
        <input type="text" name="name" id="name" placeholder="👤 Enter your name" />
        <input type="password" name="password" id="password" placeholder="🔑 Enter your password" />
        <button type="submit" className="submit">Login</button>

      </form>
    </div>
  );
}

export default App;
