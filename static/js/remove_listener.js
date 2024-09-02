function removeClickListener(element) {
  if (element && typeof element.removeEventListener === "function") {
    element.removeEventListener("click", function handleClick() {
      // This is the event listener function that was originally attached
      console.log("Button clicked! (This message won't be shown after removal)");
    });
  } else {
    console.error("Invalid element or missing removeEventListener function");
  }
}
