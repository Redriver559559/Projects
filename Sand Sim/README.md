<h1>General Information</h1>
<p>This sand sim is currently being updated and it currently has some bugs and issues. You can create your own particles / elements and add your own spinoff. Using the top row numbers 1-6 you can switch between different types of particles such as Fire, Thermite, Water, Liquid Nitrogen, and more. This is a learning experience so some things may take time, for example coding a color map for each particle so they change colors in different states and temperatures. </p>

---

<img src="https://user-images.githubusercontent.com/69123362/189286714-8ec51c0e-ca17-4418-91c4-d5874a2b656e.png">
<h1>Technical Aspects</h1>
<p>Currently there are no optimizations such as multithreading / processing and there is no chunking. I plan to add it on a more stable version of this project eventually. Heat is spread using a blur method (Just averaging close nieghbors) to cakculate and change the temperature of each particle. Other than that, it is just using some simple rules and the use of Pygame for rendering and taking user input for now. </h1>
