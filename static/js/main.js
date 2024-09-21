// Function to display current time
function updateTime() {
    const timeElement = document.getElementById('current-time');
    const now = new Date();
    const timeString = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
    timeElement.textContent = `Current Time: ${timeString}`;
}

setInterval(updateTime, 1000); // Update time every second

// Scrolling text
//function startScrollingText() {
//    const scrollingText = document.getElementById('scrolling-text');
//    scrollingText.style.animation = "scrolling 10s linear infinite";
//}
//
//window.onload = startScrollingText;

// New function for showing an access denied popup
function accessDenied() {
    alert("Access is blocked. You do not have permission to access this page.");
}
