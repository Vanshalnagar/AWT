const event = require("events")

const em = new event.EventEmitter()

let login = 0
let logout = 0
let purchase = 0
let update = 0

em.on("login", (user) => {
    login++
    console.log(user + " logged in")
})

em.on("logout", (user) => {
    logout++
    console.log(user + " logged out")
})

em.on("purchase", (user, item) => {
    purchase++
    console.log(user + " bought " + item)
})

em.on("update", (user, field) => {
    update++
    console.log(user + " updated " + field)
})

em.on("summary", () => {
    console.log("\nSummary")
    console.log("login:", login)
    console.log("logout:", logout)
    console.log("purchase:", purchase)
    console.log("update:", update)
})

em.emit("login", "Vanshal Nagar")
em.emit("login", "Vanshal Nagar")
em.emit("purchase", "Vanshal Nagar", "Laptop")
em.emit("update", "Vanshal Nagar", "Email")
em.emit("logout", "Vanshal Nagar")
em.emit("purchase", "Vanshal Nagar", "Phone")
em.emit("update", "Vanshal Nagar", "Password")
em.emit("logout", "Vanshal Nagar")

em.emit("summary")
