// ************ To remove the error message and cross : ******

const notify_msg = document.getElementById('notify_msg');

// Function to hide the message after 4s
if (notify_msg) {
  setTimeout(() => {
    notify_msg.style.display = 'none';
  }, 4000); // 4000ms = 4s
}