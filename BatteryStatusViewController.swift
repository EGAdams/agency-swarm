import Foundation
import UIKit

class BatteryStatusViewController: UIViewController {
    @IBOutlet var tableView: UITableView!
    var dataSource: BatteryStatusDataSource!
    override func viewDidLoad() {
        super.viewDidLoad()
        dataSource = BatteryStatusDataSource()
        tableView.dataSource = dataSource
        tableView.reloadData()
    }
}