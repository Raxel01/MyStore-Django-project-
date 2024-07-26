const fetchProduct1 = async  ()=>{
    const url = 'http://127.0.0.1:4000/store/products/1/'

// const response = await fetch(url)

try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const json = await response.json();
    console.log(json);
  } catch (error) {
    console.error(error.message);
  }
}

fetchProduct1()