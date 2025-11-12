import Foundation


func readF(path: String) -> [[String]] {
        let content = try! String(contentsOfFile: path, encoding: .utf8)
        let lines = content.components(separatedBy: .newlines)
        
        let l1 = lines[0].components(separatedBy: ",")
        let l2 = lines[2].components(separatedBy: ",")

        return [l1,l2]
}


let data = readF(path: "./notes1.txt")

print(data[0])
print(data[1])

//print(data[0].count)


let size = data[0].count
var p = 0

print(p)

for i in data[1] {
    let chars = Array(i)
    let d = String(chars[0])
    let n = Int(String(chars[1]))!

    switch d {
        case "L":
            print("L")
            p = p - n
            if(p < 0) {
                p = 0
            }
            print(p)
        case "R":
            print("R")
            p = p + n
            if (p > size-1){
                p = size-1
            }
            print(p)
        default:
            print("x")
    }
} 


print(data[0][p])
