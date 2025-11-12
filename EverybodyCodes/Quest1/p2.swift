import Foundation


func readF(path: String) -> [[String]] {
        let content = try! String(contentsOfFile: path, encoding: .utf8)
        let lines = content.components(separatedBy: .newlines)
        
        let l1 = lines[0].components(separatedBy: ",")
        let l2 = lines[2].components(separatedBy: ",")

        return [l1,l2]
}

func mod(_ a: Int, _ n: Int) -> Int {
    let r = a % n
    return r >= 0 ? r : r + n
}


let data = readF(path: "./notes2.txt")

print(data[0])
print(data[1])

//print(data[0].count)


let size = data[0].count;
var p = 0

print("size: ")
print(data[0].count)
print("---")

print(p)

for i in data[1] {
    let chars = Array(i)
    let d = String(chars[0])
    let n = Int(String(chars[1...]))!
    switch d {
        case "L":     
            p = mod(p-n, size)
        case "R":
            p = mod(p+n, size)
        default:
            print("x")
    }


    print("Instruccion: \(i), P: \(p), arreglo en \(data[0][p])")
} 

print(data[0][p])
