import Foundation
import UIKit

class BatteryStatusDataSource: NSObject, UITableViewDataSource {
    let data = [
        (time: "09:00", date: "28/07/2023", batteryLevel: "100%", batteryState: "Charging"),
        (time: "11:00", date: "28/07/2023", batteryLevel: "90%", batteryState: "Discharging"),
        (time: "15:00", date: "28/07/2023", batteryLevel: "75%", batteryState: "Charging")
    ]
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return data.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "BatteryCell", for: indexPath)
        let item = data[indexPath.row]
        cell.textLabel?.text = item.time + ", " + item.date
        cell.detailTextLabel?.text = item.batteryLevel + ", " + item.batteryState
        return cell
    }
}