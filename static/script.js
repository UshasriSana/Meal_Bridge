// Calculate time left until expiry
function timeLeft(expiryTime) {
    const expiry = new Date(expiryTime).getTime();
    const now = new Date().getTime();
    const diff = expiry - now;

    if (diff <= 0) {
        return "Expired";
    }

    const hours = Math.floor(diff / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));

    return `${hours}h ${minutes}m left`;
}

// Update all time-left fields
function updateTimers() {
    document.querySelectorAll(".expiry-time").forEach(el => {
        const expiry = el.dataset.expiry;
        el.innerText = timeLeft(expiry);
    });
}

// Auto refresh receiver page every 60 seconds
setInterval(() => {
    if (window.location.pathname === "/receiver") {
        location.reload();
    }
}, 60000);

// Run timer updates every minute
setInterval(updateTimers, 60000);
updateTimers();
