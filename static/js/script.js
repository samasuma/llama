document.getElementById('questionForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission
  
    var questionInput = document.getElementById('questionInput').value;
  
    axios.post('/api/query', {
      question: questionInput
    })
    .then(function(response) {
      document.getElementById('answer').innerText = response.data.answer;
    })
    .catch(function(error) {
      console.error('Error:', error);
      document.getElementById('answer').innerText = 'Error fetching answer.';
    });
  });
  