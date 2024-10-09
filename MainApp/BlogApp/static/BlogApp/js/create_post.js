document.addEventListener("DOMContentLoaded", function() {
    // Getting the necessary elements
    const descriptionInput = document.querySelector('.tweet-input');
    const charCount = document.getElementById('charCount');
    const tweetButton = document.getElementById('tweetButton');
    const styledText = document.getElementById('styledText');

    // Function to auto-resize textarea height
    function autoResize() {
        descriptionInput.style.height = 'auto';  // Reset the height
        descriptionInput.style.height = descriptionInput.scrollHeight + 'px';  // Set height based on content
    }

    // Function to handle hashtag styling in the hidden div
    function handleHashtagStyling() {
        const text = descriptionInput.value;
        const formattedText = text.replace(/(#[a-zA-Z0-9_]+)/g, '<span class="hashtag">$1</span>');
        styledText.innerHTML = formattedText;
    }

    // Listening for input in the textarea (form.description)
    descriptionInput.addEventListener('input', function() {
        const tweetLength = descriptionInput.value.length;

        // Update the character count
        charCount.textContent = tweetLength;

        // Enable or disable the Post button based on input length
        tweetButton.disabled = tweetLength === 0;

        // Apply hashtag styling
        handleHashtagStyling();

        // Auto-resize the textarea height
        autoResize();
    });
    descriptionInput.addEventListener('input', function() {
        descriptionInput.style.height = 'auto';  // Reset the height
        descriptionInput.style.height = descriptionInput.scrollHeight + 'px';  // Set the height based on content
});
});

// Auto-resize textarea to match content height

