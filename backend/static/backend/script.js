// Example: Add interactivity to the search bar
document.getElementById('search-button').addEventListener('click', () => {
    const searchQuery = document.getElementById('search-input').value;
    if (searchQuery) {
      alert(`You searched for: ${searchQuery}`);
      // You can add logic to filter or fetch news based on the search query
    } else {
      alert('Please enter a search term.');
    }
  });